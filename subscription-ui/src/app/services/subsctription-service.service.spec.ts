import { TestBed } from '@angular/core/testing';

import { SubsctriptionService } from './subsctription-service.service';

describe('SubsctriptionServiceService', () => {
  let service: SubsctriptionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SubsctriptionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
