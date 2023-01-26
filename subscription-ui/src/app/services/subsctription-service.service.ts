import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http'

import { API_URL } from 'src/environments/environment';
import { IUser } from '../interface/user';
import { INotification } from '../interface/notification';
import { IStatus } from '../interface/status';


@Injectable({
  providedIn: 'root'
})
export class SubsctriptionService {

  constructor( private httpClient: HttpClient) { }

  private api = API_URL
  
  public getStatus(user: string){
    return this.httpClient.get<IStatus>(this.api + 'getUserStatus/' + user);
  }

  public createAccount(user: IUser){
    return this.httpClient.post(this.api + 'users/createAccount/', user);
  }

  public login(user: IUser){
    return this.httpClient.post(this.api + 'users/login/', user);
  }

  public sendNotification(notification: INotification){
    return this.httpClient.post(this.api + 'send_requisition/', notification)
  }
}
