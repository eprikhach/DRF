import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SigninComponent } from './signin/signin.component';
import { SignupComponent } from './signup/signup.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { AuthGuard } from "./shared/auth.guard";
import {CreateCourseComponent} from "./create-course/create-course.component";
// import {CreateTicketComponent} from "./create-ticket/create-ticket.component";

const routes: Routes = [
  { path: '', redirectTo: '/user-profile', pathMatch: 'full' },
  { path: 'log-in', component: SigninComponent },
  { path: 'sign-up', component: SignupComponent },
  { path: 'user-profile', component: UserProfileComponent, canActivate: [AuthGuard] },
  { path: 'create-course', component: CreateCourseComponent}
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }