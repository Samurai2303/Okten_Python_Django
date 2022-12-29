import {Component, OnInit} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {ICar} from "../interfaces";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'my_frontend';

  cars: any

  constructor(private httpClient:HttpClient) {
  }

  ngOnInit(): void {
    this.httpClient.get<any>('/api/cars').subscribe(value => this.cars = value)
  }





}
