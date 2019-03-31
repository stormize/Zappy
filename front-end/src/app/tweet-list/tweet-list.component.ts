import { Component, OnInit } from '@angular/core';
import {tweet} from '../tweet';
import {Observable} from 'rxjs';
import {ApiService} from '../api.service';
@Component({
  selector: 'app-tweet-list',
  templateUrl: './tweet-list.component.html',
  styleUrls: ['./tweet-list.component.css']
})
export class TweetListComponent implements OnInit {
  tweets:Observable<tweet[]>
  constructor(private apiservice:ApiService) { }
  ngOnInit() {
    
    this.getTweets()
  }

  
  public getTweets(){
    this.tweets=this.apiservice.getTasks(null)
  }
}
