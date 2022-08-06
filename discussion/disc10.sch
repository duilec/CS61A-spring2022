;q1
(define (vir-fib n)
    'YOUR-CODE-HERE
    (cond
        ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (vir-fib (- n 1)) (vir-fib (- n 2))))
    )
)

(expect (vir-fib 2) 1)
(expect (vir-fib 10) 55)
(expect (vir-fib 1) 1)

;q2
(define with-list
    (list(list 'a 'b) 'c 'd (list 'e))
)
(draw with-list)

(define with-quote
    '((a b) c d (e))
)
(draw with-quote)

(define helpful-list
   (cons 'a (cons 'b nil)))
(draw helpful-list)

(define another-helpful-list
    (cons 'c (cons 'd (cons (cons 'e nil) nil))))
(draw another-helpful-list)

(define with-cons
    (cons
        (cons 'a (cons 'b nil)) (cons 'c (cons 'd (cons (cons 'e nil) nil)))
    )
)
(draw with-cons)

;q3
(define (list-concat a b)
    (if (null? a) 
        b
        (cons (car a) (list-concat (cdr a) b))
    )
)

(expect (list-concat '(1 2 3) '(2 3 4)) (1 2 3 2 3 4))
(expect (list-concat '(3) '(2 1 0)) (3 2 1 0))

;q4
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

;q5
;not use 'filter'
;build a new list
;we don't concat 'item', just remove continue
(define (remove item lst)
  (cond
      ((eq? lst nil) nil)
      ((not (= item (car lst))) (cons (car lst) (remove item (cdr lst))))
      ((= item (car lst)) (remove item (cdr lst)))
  )
)

(expect (remove 3 nil) ())
(expect (remove 2 '(1 3 2)) (1 3))
(expect (remove 1 '(1 3 2)) (3 2))
(expect (remove 42 '(1 3 2)) (1 3 2))
(expect (remove 3 '(1 3 3 7)) (1 7))

;q5-sol
(define (remove item lst)
  (cond ((null? lst) '())
        ((equal? item (car lst)) (remove item (cdr lst)))
        (else (cons (car lst) (remove item (cdr lst)))))
)

(expect (remove 3 nil) ())
(expect (remove 2 '(1 3 2)) (1 3))
(expect (remove 1 '(1 3 2)) (3 2))
(expect (remove 42 '(1 3 2)) (1 3 2))
(expect (remove 3 '(1 3 3 7)) (1 7))