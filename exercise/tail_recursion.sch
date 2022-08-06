;; Return the nth Fibonacci number.
(define (fib n)
    (define (fib-iter current k)
        (if (= k n)
            current
            (fib-iter (+ current (fib (- k 1))) (+ k 1))
        ) 
    )
    (if (= 1 n) 0 (fib-iter 1 2)))

(define (map procedure s)
    (define (map-reverse s m)
        (if (null? s)
            m
            (map-reverse (cdr s) (cons (procedure (car s)) m))
        )
    )
    (reverse (map-reverse s nil))
)

(define (reverse s)
    (define (reverse-iter s r)
    (if (null? s)
        r
        (reverse-iter (cdr s) (cons (car s) r))))
    (reverse-iter s nil))

(map (lambda (x) (- 5 x)) (list 1 2))