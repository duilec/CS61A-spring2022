(define (north_of_eq point)
    (> (car point) 0)
)
(expect (north_of_eq '(67 10)) #t)
(expect (north_of_eq '(67 -10)) #t)
(expect (north_of_eq '(-67 10)) #f)
(expect (north_of_eq '(-67 -10)) #f)

(define (all_north_of_eq points)
    (if (> (car (car points)) 0)
        (if (> (car (car (cra points))) 0))
            (if (> (car (cra (cra points))) 0) #t #f)
        #f
    #f
    )
)

;solution
;use recursion
;use func of 'north_of_eq'
(define (all_north_of_eq points)
    (cond 
        ( (null? points) #t)
        ( (north_of_eq (car points)) (all_north_of_eq (cdr points)) )
        (else #f)
    )
)

;solution
;use filter
;(filter <pred> <lst>)
;filter: Returns a list consisting of only the elements of lst that return true when called on pred (a one-argument procedure).
;use func of 'north_of_eq'
(define (all_north_of_eq points)
    (= (length (filter north_of_eq points)) (length points))   
)

(expect (all_north_of_eq '( (67 10) (14 43) (37 -122))) #t)
(expect (all_north_of_eq '( (-67 10) (14 43) (37 -122))) #f)
(expect (all_north_of_eq '( (67 10) (14 43) (-37 -122))) #f)
(expect (all_north_of_eq '()) #t)

;mysolution
(define (countdown_list n)
    (cond
        ((> n 0) (cons n (countdown_list (- n 1))))
        (else nil)
    )
)

(expect (countdown_list 3) (3 2 1))
(expect (countdown_list 1) (1))

;reference solution
(define (countdown_list n) 
    (if
        (= n 0) nil
        (cons n (countdown_list (- n 1)))
    )
)

(expect (countdown_list 3) (3 2 1))
(expect (countdown_list 1) (1))

;mysolution
;use 'append'
(define (countup_list n) 
    (if
        (= n 1) cons 1
        (append (countup_list (- n 1)) (cons n nil))
    )
)

(expect (countup_list 3) (1 2 3))
(expect (countup_list 1) (1))

;reference solution
;head is nil?
(define (countup_list n) 
    (if
        (= n 0) nil
        (append (countup_list (- n 1)) (cons n nil) )
    )
)
                    
(expect (countup_list 3) (1 2 3))
(expect (countup_list 1) (1))

(if (or #t (/ 1 0)) 1 (/ 1 0))
((if (< 4 3) + -) 4 100)

