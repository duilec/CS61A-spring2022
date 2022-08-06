; Q5: Group by Non-Decreasing
; note: using "(null? (cdr s)" in "(sublist s)" and "(rest s)"
;       because "(cadr s)" need a not null rest of list to get value
; big idea of my solution: get the sub list and rest list in the same time
(define (nondecreaselist s)
    (define (cadr s)
        (car (cdr s))
    )
    (define (sublist s)
        (cond
            ((null? (cdr s)) (cons (car s) nil))
            ((<= (car s) (cadr s)) (cons (car s) (sublist (cdr s))))
            (else (cons (car s) nil))
        )
    )
    (define (rest s)
        (cond
            ((null? (cdr s)) nil)
            ((<= (car s) (cadr s)) (rest (cdr s)))
            (else (cdr s))
        )
    )
    (cond
        ((null? s) nil)
        (else (cons (sublist s) (nondecreaselist (rest s))) )
    )
)

(expect (nondecreaselist '(1 2 3 1 2 3)) ((1 2 3) (1 2 3)))

(expect (nondecreaselist '(1 2 3 4 1 2 3 4 1 1 1 2 1 1 0 4 3 2 1))
        ((1 2 3 4) (1 2 3 4) (1 1 1 2) (1 1) (0 4) (3) (2) (1)))



; reference
; note: (list 1) equals (cons 1 nil)
; not easily to figure out
; passes "(car rest)" and "(cdr rest)" each time(line: 46), end or restart from "rest"(line: 45)
(define (nondecreaselist s)
    (if (null? s) 
        nil 
        (let ((rest (nondecreaselist (cdr s)) )) 
            (if (or (null? (cdr s)) (> (car s) (car (cdr s)))) 
                (cons (list (car s)) rest) 
                (cons (cons (car s) (car rest)) (cdr rest))
            ) 
        ) 
    ) 
)

;Q6: To Scheme An Environment Diagram

;Q6.1
;The Global frame
;since that is where the lambda procedure was defined.

;The Global frame
;since that is where the mu procedure was called

;Q6.2
;note: "by" equals "depend on" in this case
;The Frame f1 is created by the call to (goat 1 2)
;The Global frame is the parent of this frame, in which the lambda procedure was defined.(it also was called)
;lexical scoping

;The Frame f2 is created by the call to (horse 1 2)
;The Global frame is the parent of this frame, in which the mu procedure was called.(it also was defined)
;dynamic scoping

;The Frame f3 is created by the call to (horse 5)
;The Frame f1 is the parent of this frame, in which the lambda procedure was defined.(it was called in the Global frame)

;The Frame f4 is created by the call to (saddle 5)
;The Global frame is the parent of this frame, in which the mu procedure was called.(it also was defined)

;the output of (horse 5) is "7" 
;the output of (saddle 5) is "25"

;There would be no difference in output, 
;since using define to define a procedure is equivalent to using define to define a variable 
;that is assigned to a lambda procedure in our version of Scheme.


;Q7: Or with Multiple Args(Programs as Data)
; note: the error message of "Error: division by zero" also is thing of "#t"
; note: list(eg. (+ 1 2)) will automatically execute and atom(eg. #f) will directly be accessed with beginning of ","
; note: use "`" to let function(program) become data
(define (make-long-or args)
    ;'YOUR-CODE-HERE
    `,(cond
        ((null? args) #f)
        ((boolean? (car args)) 
            (if (eq? (car args) #t)
                #t
                (make-long-or (cdr args))
            )
        )
        (else (car args))
    )
)

;Q7 test
;scm> (define or-program (make-long-or '((print 'hello) (/ 1 0) 3 #f)))
;or-program
;scm> (eval or-program)
;hello
;scm> (eval (make-long-or '((= 1 0) #f (+ 1 2) (print 'goodbye))))
;3
;scm> (eval (make-long-or '((> 3 1))))
;#t
;scm> (eval (make-long-or '()))
;#f

;Q7 reference
;you can use "let" when you would to let function(program) become data
;(define (make-long-or args) 
;    (cond
;        ((null? args) #f) 
;        (else
;            `(let ((v1 ,(car args))) 
;                (if v1 
;                    v1 
;                    ,(make-long-or (cdr args))
;                )
;            )
;        ) 
;    ) 
;)

