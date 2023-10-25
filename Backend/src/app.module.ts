import { Module } from '@nestjs/common';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { EnvironmentVariables, validateEnv } from './_utils/config/config';
import { HelloworldModule } from './helloworld/helloworld.module';
import { LogsModule } from './logs/logs.module';
import { DashboardModule } from './dashboard/dashboard.module';
import { ContainersModule } from './containers/containers.module';
import { BlacklistModule } from './blacklist/blacklist.module';
import { UserModule } from './user/user.module';
import { MongooseModule } from '@nestjs/mongoose';
import { GlobalModule } from './_utils/global.module';
import { MailsModule } from './mails/mails.module';

@Module({
  imports: [
    GlobalModule,
    MongooseModule.forRootAsync({
      imports: [ConfigModule],
      inject: [ConfigService],
      useFactory: async (configService: ConfigService<EnvironmentVariables, true>) => ({
        uri: configService.get('MONGODB_URL'),
        autoIndex: true,
      }),
    }),
    ConfigModule.forRoot({ validate: validateEnv, isGlobal: true }),
    HelloworldModule,
    MailsModule,
    LogsModule,
    DashboardModule,
    ContainersModule,
    BlacklistModule,
    UserModule,
  ],
})
export class AppModule {}
