(define-macro (assign sym1 sym2 expr1 expr2)
  `(begin
     (define ,sym1 ,expr1)
     (define ,sym2 ,expr2)))


(define-macro (assign sym1 sym2 expr1 expr2)
  `(begin
     (define temp1 ,expr1)
     (define temp2 ,expr2)
     (define ,sym1 temp1)
     (define ,sym2 temp2)))

(define-macro (switch expr cases)
    `(let ((val ,expr))
	  ,(cons
	    `cond
	    (map (lambda (case) (cons
               `(equal? ,expr ,(car case))
		       (cdr case)))
		     cases))))