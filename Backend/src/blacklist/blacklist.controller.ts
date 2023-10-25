import { Controller } from '@nestjs/common';
import { BlacklistService } from './blacklist.service';
import { GrpcMethod } from '@nestjs/microservices';
import { ServerUnaryCall } from '@grpc/grpc-js';
import { GetIdsDto } from './_utils/dto/response/get-ids.dto';
import { ApiTags } from '@nestjs/swagger';
import { SetIpDto } from './_utils/dto/request/set-ip.dto';

@Controller('blacklist')
@ApiTags('Blacklist')
export class BlacklistController {
  constructor(private readonly blacklistService: BlacklistService) {}

  @GrpcMethod('Blacklist', 'GetBlackList')
  getBlacklist$(_data: unknown, _metadata: unknown, call: ServerUnaryCall<unknown, GetIdsDto>) {
    return this.blacklistService.getBlackList$(call);
  }

  @GrpcMethod('Blacklist', 'PutBlackList')
  PutBlackList(setIdDto: SetIpDto) {
    return this.blacklistService.putBlackList(setIdDto);
  }

  @GrpcMethod('Blacklist', 'PutWhiteList')
  PutWhiteList(setIdDto: SetIpDto) {
    return this.blacklistService.putWhiteList(setIdDto);
  }
}
