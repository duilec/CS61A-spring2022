(define (cddr s) (cdr (cdr s)))

(define (cadr s) 
    'YOUR-CODE-HERE
    (car (cdr s))
)

(define (caddr s) 
    'YOUR-CODE-HERE
    (car(cddr s))    
)

;recursion condition: (<= (car lst) (cadr lst))
;base condition: (null? (cdr lst)) or (> (car lst) (cadr lst))
(define (ascending? lst) 
    'YOUR-CODE-HERE
    (cond
        ((null? (cdr lst)) #t)
        ((> (car lst) (cadr lst)) #f)
        ((<= (car lst) (cadr lst)) (ascending? (cdr lst)))
    )
)

;note: lst1/2 already has 'cons'
(define (interleave lst1 lst2) 
    'YOUR-CODE-HERE
    (cond
        ((and (null? lst1) (null? lst2)) nil)
        ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2)))))
    )
)

;note: my-filter will reture a list that hs 'cons' when you use recursion
(define (my-filter func lst) 
    'YOUR-CODE-HERE
    (cond
        ((null? lst) nil)
        ((func (car lst)) (cons (car lst) (my-filter func (cdr lst))))
        (else (my-filter func (cdr lst)))
    )
)

;check-newlst, #t => can insert element, #f => can't insert element
;insert-newlst, recursion to make a no-repeats lst
    ;in insert-newlst, newlst is a reversed list comparing answer list 
(define (no-repeats lst) 
    'YOUR-CODE-HERE
    (define (insert-newlst lst newlst)
        (define (check-newlst element newlst)
            (cond
                ((null? newlst) #t)
                ((= element (car newlst)) #f)
                (else (check-newlst element (cdr newlst)))
            )
        )
        (cond
            ((null? lst) nil)
            ((check-newlst (car lst) newlst) (cons (car lst) (insert-newlst (cdr lst) (cons (car lst) newlst))))
            (else (insert-newlst (cdr lst) newlst))
        )
    )
    (insert-newlst lst nil)
)
