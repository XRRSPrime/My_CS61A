(define (ascending? s) 
    (if (or (null? s) (null? (cdr s)))
        #t
        (if (> (car s) (car (cdr s)))
            #f
            (ascending? (cdr s)))))

(define (my-filter pred s) 
    (if (null? s)
        s 
        (if (pred (car s))
            (append (list (car s)) (my-filter pred (cdr s)))
            (my-filter pred (cdr s)))))

(define (interleave lst1 lst2)
    (if (and (not (equal? lst1 nil)) (not (equal? lst2 nil)))
        (append (list (car lst1) (car lst2)) (interleave (cdr lst1) (cdr lst2)))
        (if (equal? lst1 nil)
            lst2
            lst1)))

(define (member num lst)
    (cond ((null? lst) #f)
          ((equal? num (car lst)) #t)
          (else (member num (cdr lst)))))

(define (no-repeats s)
    (if (null? s)
        '()
        (let ((current (car s))
              (rest (cdr s)))
            (if (member current rest)
                (no-repeats rest)
                (cons current (no-repeats rest))))))
