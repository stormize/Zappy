import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TweetListComponent } from './tweet-list/tweet-list.component';
import {TimeAgoPipe} from 'time-ago-pipe';
import { from } from 'rxjs';



@NgModule({
  declarations: [
    AppComponent,
    TweetListComponent,
    TimeAgoPipe,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
