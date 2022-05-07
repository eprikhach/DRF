import { Injectable } from '@angular/core';
import {User} from "./user";
import {Observable, of, tap} from "rxjs";
import {HttpClient} from "@angular/common/http";
import {catchError} from "rxjs/operators";
import {AuthService} from "./auth.service";

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private api = 'http://localhost:8000/api'

  constructor(
        private http: HttpClient,
        public authService: AuthService
  )
  { }


  searchUsers(term: string): Observable<User[]> {
        if (!term.trim()) {
            // if not search term, return empty hero array.
            return of([]);
        }
        return this.http.get<User[]>(`${this.api}/filtering_user/users/${term}/`).pipe(
            tap(x => x.length ?
                console.log(`found users matching "${term}"`) :
                console.log(`no users matching "${term}"`)),
            catchError(this.authService.handleError)
        );
    }
}
