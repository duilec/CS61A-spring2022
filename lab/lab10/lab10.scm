(define (over-or-under num1 num2) 
    'YOUR-CODE-HERE
    (cond ((< num1 num2) -1) 
          ((= num1 num2) 0) 
          (else 1)
    )
)
;use if
;   (if (< num1 num2) -1
;   (if (= num1 num2) 0 1)
;   )

;we will ret a lambda
(define (make-adder num) 
    'YOUR-CODE-HERE
    (lambda (x) (+ x num))
)

;we need a input
;we should ret a lambda
(define (composed f g) 
    'YOUR-CODE-HERE
    (lambda (x) (f (g x)))
)


; be care of using '( )', it has meaning and can't be uselessful
; eg. 
; (* (square base) (pow base (- exp 2))) not equals ((* (square base) (pow base (- exp 2))))
(define (square n) (* n n))

(define (pow base exp) 
    'YOUR-CODE-HERE
    (if (= base 1)
        1
        (if (= exp 0) 
            1
            (if (even? exp)
                (* (square base) (pow base (- exp 2)))
                (* base (pow base (- exp 1)))
            )
        )
    )
)

;other solution
            ;(if (even? exp)
                ;(square (pow base (/ exp 2)))  
                ;(* base (square (pow base (/ (- exp 1) 2))))  
            ;)


(define (vir-fib n)
    'YOUR-CODE-HERE
    (cond
        ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (vir-fib (- n 1)) (vir-fib (- n 2))))
    )
)
;when you test online, you must use 'expect'
(expect (vir-fib 10) 55)
(expect (vir-fib 1) 1)

;q5
;build a new list
(define (map-fn fn lst)
    'YOUR-CODE-HERE
    (cond
        ((null? lst) nil)
        (else (cons (fn (car lst)) (map-fn fn (cdr lst))))
    )
)

(map-fn (lambda (x) (* x x)) '(1 2 3))
;expect (1 4 9)
;you should keep commit of ';expect (1 4 9)'