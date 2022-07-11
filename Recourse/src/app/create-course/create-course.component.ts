import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {Router} from '@angular/router';
import {TicketService} from "../shared/ticket.service";
import {UserService} from "../shared/user.service";
import {debounceTime, distinctUntilChanged, Observable, Subject, switchMap} from "rxjs";
import {User} from "../shared/user";
import {AuthService} from '../shared/auth.service';
import {COMMA, ENTER} from '@angular/cdk/keycodes';
import {ElementRef, ViewChild} from '@angular/core';
import {FormControl} from '@angular/forms';
import {MatAutocompleteSelectedEvent} from '@angular/material/autocomplete';
import {MatChipInputEvent} from '@angular/material/chips';
import {map, startWith} from 'rxjs/operators';

@Component({
    selector: 'app-create-course',
    templateUrl: './create-course.component.html',
    styleUrls: ['./create-course.component.sass']
})
export class CreateCourseComponent implements OnInit {
    users$!: Observable<User[]>
    private searchTerms = new Subject<string>()
    currentUser: User = new User()
    ticketForm: FormGroup;
    separatorKeysCodes: number[] = [ENTER, COMMA];
    fruitCtrl = new FormControl();
    filteredFruits: Observable<string[]>;
    fruits: string[] = ['Lemon'];
    allFruits: string[] = ['Apple', 'Lemon', 'Lime', 'Orange', 'Strawberry'];
    isLinear = false;
    courseName!: FormGroup;
    courseDescribe!: FormGroup;

    @ViewChild('fruitInput') fruitInput?: ElementRef<HTMLInputElement>;


    constructor(
        public authService: AuthService,
        public fb: FormBuilder,
        public router: Router,
        public ticketService: TicketService,
        private userService: UserService,
    ) {
        this.authService.getUserProfile().subscribe((res: any) => {
            this.currentUser = res;
        });
        this.ticketForm = this.fb.group({
            subject: [''],
            ticket_status: [''],
            description: [''],
            supports: ['']
        });
        this.filteredFruits = this.fruitCtrl.valueChanges.pipe(
            startWith(null),
            map((fruit: string | null) => (fruit ? this._filter(fruit) : this.allFruits.slice())),)
    }

    ngOnInit() {
        this.courseName = this.fb.group({
            name: ['', Validators.required],
        });
        this.courseDescribe = this.fb.group({
            description: ['', Validators.required],
        });
        this.users$ = this.searchTerms.pipe(
            // wait 300ms after each keystroke before considering the term
            debounceTime(300),

            // ignore new term if same as previous term
            distinctUntilChanged(),

            // switch to new search observable each time the term changes
            switchMap((term: string) => this.userService.searchUsers(term)),
        );
    }

    search(term: string): void {
        this.searchTerms.next(term);
    }

    add(event: MatChipInputEvent): void {
        const value = (event.value || '').trim();

        // Add our fruit
        if (value) {
            this.fruits.push(value);
        }

        // Clear the input value
        event.chipInput!.clear();

        this.fruitCtrl.setValue(null);
    }

    remove(fruit: string): void {
        const index = this.fruits.indexOf(fruit);

        if (index >= 0) {
            this.fruits.splice(index, 1);
        }
    }

    selected(event: MatAutocompleteSelectedEvent): void {
        this.fruits.push(event.option.viewValue);
        this.fruitInput!.nativeElement!.value = '';
        this.fruitCtrl.setValue(null);
    }

    private _filter(value: string): string[] {
        const filterValue = value.toLowerCase();

        return this.allFruits.filter(fruit => fruit.toLowerCase().includes(filterValue));
    }

    createTicket() {
        this.ticketForm.value.supports = this.ticketForm.value.supports.split(',')
        this.ticketService.createTicket(this.ticketForm.value).subscribe((res) => {
            if (res.result) {
                console.log('okay')
            }
        })
    }
    createCourse() {
        const finalData = {...this.courseName.value, ...this.courseDescribe.value};
        // this.courseData = Object.assign({}, this.courseName.value, this.courseDescribe.value)
        console.log(finalData)
        this.ticketService.createTicket(finalData)
            .subscribe((res) => {
            if (res.result) {
                this.courseName.reset();
                this.courseDescribe.reset();

            }
        });
        this.router.navigate(['../home'])
    }


}

