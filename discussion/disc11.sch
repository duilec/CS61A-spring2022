;q1
;a: not tail recursion
;b: yes, it is tail recursion
;c: error, infinite recursion
;d: error, infinite recursion
;e; yse, it is tail recursion

;q2
;add another argu --> 'num'
(define (sum lst)
  'YOUR-CODE-HERE
  (define (sum-tail lst num)
    (cond
      ((null? lst) num)
      (else (sum-tail (cdr lst) (+ num (car lst))))
    )
  )
  (sum-tail lst 0)
)

(expect (sum '(1 2 3)) 6)
(expect (sum '(10 -3 4)) 11)

;q3
;Hint: use a helper function!
(define (reverse lst)
  'YOUR-CODE-HERE
  (define (reverse-tail lst reverse_lst)
    (cond
      ((null? lst) reverse_lst)
      (else (reverse-tail  (cdr lst) (cons (car lst) reverse_lst)))
    )
  )
  (reverse-tail lst nil)
)

(expect (reverse '(1 2 3)) (3 2 1))
(expect (reverse '(0 9 1 2)) (2 1 9 0))

;q4

