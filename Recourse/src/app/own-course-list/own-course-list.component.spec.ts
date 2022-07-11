import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OwnCourseListComponent } from './own-course-list.component';

describe('OwnCourseListComponent', () => {
  let component: OwnCourseListComponent;
  let fixture: ComponentFixture<OwnCourseListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OwnCourseListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OwnCourseListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
