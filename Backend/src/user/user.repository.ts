import { Injectable } from '@nestjs/common';
import { Model, Types } from 'mongoose';
import { InjectModel } from '@nestjs/mongoose';
import { User, UserDocument } from './user.schema';
import { hashSync } from 'bcrypt';
import { RpcException } from '@nestjs/microservices';
import { status } from '@grpc/grpc-js';
import { RoleEnum } from './_utils/enums/role.enum';

@Injectable()
export class UserRepository {
  constructor(@InjectModel(User.name) private model: Model<UserDocument>) {}

  createIfNotExist = (email: string, password: string) =>
    this.model
      .findOneAndUpdate(
        { email: email },
        {
          $set: {
            password: hashSync(password, 10),
            admin: true,
            activated: true,
            roles: [RoleEnum.ADMIN],
          },
        },
        {
          upsert: true,
          new: true,
          setDefaultsOnInsert: true,
        },
      )
      .exec();

  findByEmail = (email: string) =>
    this.model
      .findOne({ email: email })
      .orFail(new RpcException({ code: status.NOT_FOUND, message: 'USER_NOT_FOUND' }))
      .exec();

  findById = (userId: string) =>
    this.model
      .findById(userId)
      .orFail(new RpcException({ code: status.NOT_FOUND, message: 'USER_NOT_FOUND' }))
      .exec();

  findAllUsers = () => this.model.find().lean().exec();

  createUser = (user: User) =>
    this.model.create({
      email: user.email,
      password: user.password && hashSync(user.password, 10),
      roles: user.roles,
      activated: user.activated,
      lan: 'en',
    });

  updateEmailByUserId = (userId: Types.ObjectId, newEmail: string): Promise<UserDocument> =>
    this.model
      .findByIdAndUpdate(userId, { email: newEmail }, { new: true })
      .orFail(new RpcException({ code: status.NOT_FOUND, message: 'USER_NOT_FOUND' }))
      .exec();

  updatePasswordByUserId = (userId: Types.ObjectId, newPassword: string): Promise<UserDocument> =>
    this.model
      .findByIdAndUpdate(userId, { password: hashSync(newPassword, 10) }, { new: true })
      .orFail(new RpcException({ code: status.NOT_FOUND, message: 'USER_NOT_FOUND' }))
      .exec();

  activateUserById = (userId: Types.ObjectId): Promise<UserDocument> =>
    this.model
      .findByIdAndUpdate(userId, { activated: true }, { new: true })
      .orFail(new RpcException({ code: status.NOT_FOUND, message: 'USER_NOT_FOUND' }))
      .exec();

  updateRightByUserEmail = (email: string, roles: RoleEnum[]): Promise<UserDocument> =>
    this.model
      .findOneAndUpdate({ email }, { roles }, { new: true })
      .orFail(new RpcException({ code: status.NOT_FOUND, message: 'USER_NOT_FOUND' }))
      .exec();

  updateDeleteByUserEmail = async (email: string) => {
    const user = await this.findByEmail(email);
    return this.updateDeleteById(user._id);
  };

  updateDeleteById = (userId: Types.ObjectId) =>
    this.model
      .findByIdAndDelete(userId)
      .orFail(new RpcException({ code: status.NOT_FOUND, message: 'USER_NOT_FOUND' }))
      .exec();

  updateLanguageByUserId = (userId: Types.ObjectId, newLanguage: string): Promise<UserDocument> => {
    return this.model
      .findByIdAndUpdate(userId, { lan: newLanguage }, {new: true})
      .orFail(new RpcException('USER_NOT_FOUND'))
      .exec();
  }
  
  updateNightModeById = (userId: Types.ObjectId, nightMode: boolean): Promise<UserDocument> =>
  this.model
    .findByIdAndUpdate(userId, { nightMode: nightMode }, { new: true })
    .orFail(new RpcException({ code: status.NOT_FOUND, message: 'USER_NOT_FOUND' }))
    .exec();
}
