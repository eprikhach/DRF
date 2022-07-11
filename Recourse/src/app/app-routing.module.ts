import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {SigninComponent} from './signin/signin.component';
import {SignupComponent} from './signup/signup.component';
import {UserProfileComponent} from './user-profile/user-profile.component';
import {AuthGuard} from "./shared/auth.guard";
import {CreateCourseComponent} from "./create-course/create-course.component";
import {MainPageComponent} from "./main-page/main-page.component";
import {OwnCourseListComponent} from "./own-course-list/own-course-list.component";
import {ShowCourseComponent} from "./show-course/show-course.component";
import {EditCourseComponent} from "./edit-course/edit-course.component";
import {CreateLectureComponent} from "./create-lecture/create-lecture.component";
// import {CreateTicketComponent} from "./create-ticket/create-ticket.component";

const routes: Routes = [
    {path: '', redirectTo: '/home', pathMatch: 'full'},
    {path: 'home', component: MainPageComponent},
    {path: 'log-in', component: SigninComponent},
    {path: 'sign-up', component: SignupComponent},
    {path: 'user-profile', component: UserProfileComponent, canActivate: [AuthGuard]},
    {path: 'create-course', component: CreateCourseComponent},
    {path: 'own-courses', component: OwnCourseListComponent},
    {path: 'course/:courseId', component: ShowCourseComponent},
    {path: 'course-upd/:courseId', component: EditCourseComponent},
    {path: ':courseId/create-lecture', component: CreateLectureComponent}

];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule {
}