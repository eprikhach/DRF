import { Component } from '@angular/core';
import { NgbCarouselConfig } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css'],
  providers: [NgbCarouselConfig]
})
export class MainPageComponent{
  title = 'ng-carousel-demo';

  images = [
    {title: 'Introducing into python GIL', short: 'Exploring python global interpreter lock step by step',
      src: "assets/img/course_img1.jpg"},
    {title: 'Docker compose for beginners', short: 'Exploring the structure of docker files',
      src: "assets/img/course_img2.jpg"},
    {title: 'Angular component types', short: 'Exploring existing types of angular components',
      src: "assets/img/course_img3.jpg"}
  ];

  constructor(config: NgbCarouselConfig) {
    config.interval = 10000;
    config.keyboard = true;
    config.pauseOnHover = true;
  }
}