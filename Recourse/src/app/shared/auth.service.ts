import {Injectable} from '@angular/core';
import {User} from './user';
import {Observable, throwError} from 'rxjs';
import {catchError, map} from 'rxjs/operators';
import {
    HttpClient,
    HttpHeaders,
    HttpErrorResponse,
} from '@angular/common/http';
import {Router} from '@angular/router';

@Injectable({
    providedIn: 'root',
})
export class AuthService {
    endpoint: string = 'http://localhost:8000/api';
    headers = new HttpHeaders({'Content-Type': 'application/json'})

    currentUser = {};

    constructor(private http: HttpClient, public router: Router) {
    }

    // Sign-up
    signUp(user: User): Observable<any> {
        let api = `${this.endpoint}/users/`;
        return this.http.post(api, user, {headers: this.headers}).pipe(catchError(this.handleError));

    }

    // Sign-in
    signIn(user: User) {
        return this.http
            .post<any>(`${this.endpoint}/jwt/create`, user)
            .subscribe((res: any) => {
                // console.log(res)

                localStorage.setItem('access_token', res['access']);
                this.getUserProfile().subscribe((res) => {
                    this.currentUser = res;
                    this.router.navigate(['home/']);
                });
            });
    }

    getToken() {
        return localStorage.getItem('access_token');
    }

    get isLoggedIn(): boolean {
        let authToken = localStorage.getItem('access_token');
        return authToken !== null;
    }

    doLogout() {
        let removeToken = localStorage.removeItem('access_token');
        if (removeToken == null) {
            this.router.navigate(['log-in']);
        }
    }

    // User profile
    getUserProfile(): Observable<any> {
        let api = `${this.endpoint}/users/me/`;
        return this.http.get(api, {headers: this.headers}).pipe(
            map((res) => {
                return res || {};
            }),
            catchError(this.handleError)
        );
    }

    isTeacher(){
        let api = `${this.endpoint}/users/me/`;
        console.log(api)
        return this.http.get(api, {headers: this.headers}).pipe(
            map((res) => {
                return res || {};
            }),

            catchError(this.handleError)
        );
    }

    // Error
    handleError(error: HttpErrorResponse) {
        let msg = '';
        if (error.error instanceof ErrorEvent) {
            // client-side error
            msg = error.error.message;
        } else {
            // server-side error
            msg = `Error Code: ${error.status}\nMessage: ${error.message}`;
        }
        return throwError(msg);
    }
}