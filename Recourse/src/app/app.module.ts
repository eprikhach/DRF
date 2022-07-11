import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {HttpClientModule, HTTP_INTERCEPTORS} from "@angular/common/http";
import { AuthInterceptor } from './shared/authconfig.interceptor';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent } from './app.component';
import { SignupComponent } from './signup/signup.component';
import { SigninComponent } from './signin/signin.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { CreateCourseComponent } from './create-course/create-course.component';
import { MainPageComponent } from './main-page/main-page.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import {MatCardModule} from "@angular/material/card";
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatMenuModule} from "@angular/material/menu";
import {MatInputModule} from "@angular/material/input";
import {MatChipsModule} from "@angular/material/chips";
import {MatAutocompleteModule} from "@angular/material/autocomplete";
import {MatIconModule} from "@angular/material/icon";
import {MatStepperModule} from "@angular/material/stepper";
import {MatButtonModule} from "@angular/material/button";
import { ShowCourseComponent } from './show-course/show-course.component';
import { OwnCourseListComponent } from './own-course-list/own-course-list.component';
import { EditCourseComponent } from './edit-course/edit-course.component';
import { CreateLectureComponent } from './create-lecture/create-lecture.component';
import { EditLectureComponent } from './edit-lecture/edit-lecture.component';


@NgModule({
    declarations: [
        AppComponent,
        SignupComponent,
        SigninComponent,
        UserProfileComponent,
        CreateCourseComponent,
        MainPageComponent,
        ShowCourseComponent,
        OwnCourseListComponent,
        EditCourseComponent,
        CreateLectureComponent,
        EditLectureComponent
    ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        ReactiveFormsModule,
        FormsModule,
        NgbModule,
        BrowserAnimationsModule,
        MatMenuModule,
        MatInputModule,
        MatChipsModule,
        MatAutocompleteModule,
        MatIconModule,
        MatStepperModule,
        MatButtonModule,
        MatCardModule,

    ],
    providers: [{
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }],
    bootstrap: [AppComponent]
})
export class AppModule {
}
