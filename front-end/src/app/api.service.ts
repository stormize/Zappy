import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import {Observable} from 'rxjs'
import {tweet} from './tweet';
@Injectable({
  providedIn: 'root'
})
export class ApiService {
  API_URL='http://127.0.0.1:8000/events/';
  constructor(private http:HttpClient) { }
  public getTasks(param): Observable<tweet[]> {
    return this.http.get<tweet[]>(this.API_URL);
  }
  
}
