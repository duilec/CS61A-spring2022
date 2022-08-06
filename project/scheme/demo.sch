(define (map f lst) 
    (if (null? lst) 
    nil 
    (cons (f (car lst)) (map f (cdr lst))))
)

(define-macro (for formal iterable body)
    (list 'map (list 'lambda (list formal) body) iterable))

(for i '(1 2 3)
    (print (* i i)))

;output
1
4
9
(None None None)