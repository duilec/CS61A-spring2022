;q1
;(1 x 3)

;x

;(1 x 3)

;(1 2 3)

;error: (1 (unquote x 3))
;answer: (1 (unquote x) 3)

;(1 x 3)

;error: (+ 1 2 3)
;answer: 6

;(1 (2) 3)

;error: (1 (+ 2 2) 3)
;answer: (1 4 3)

;y

;(x (* 3 2) 3)
;(x 6 y)

;error: (1, (cons 2 (list 3 4)) 5)
;answer: (1 (2 3 4) 5)

;conclusion:
;in "`(...)"
;-- ',' just deal with a agrument(num, symbol or list) in quasiquote
;-- after ',' deal with a agru, if it is a call exprssion, we will execute it

;q2
;add-numbers

;(+ 1 2)

;error: (+ 1 2)
;answer: 3
;note: evaluate a expr with some builtin functions will execute it to get a value

;3
;YES, Is this similar to the previous eval call

;expr

;(lambda (a b) (+ a b))

;adder-func

;3

;make-list

;error: (list (1 2 3))
;answer: (list 1 2 3)
;note: if we concat a thing to a list without its parenthesis, we must use 'cons'
;in this case: we concat a char('list) to a list('(1 2 3)) without its parenthesis

;(1 2 3)

;(1 2 3)
;YES, Is this similar to the previous eval call

;q3
;note: use 'list' to separate different list
(define (geom n f)
    'YOUR-CODE-HERE
    (if (= n 1)
        (list '* n f)
        (list '* (geom (- n 1) f) f)   
    )
)

;solution
(define (geom n f)
    'YOUR-CODE-HERE
    (if (= n 0)
        1
        (list '* (geom (- n 1) f) f)   
    )
)

(define expr (geom 1 5))
(expect expr (* 1 5))
(expect (eval expr) 5)

(define expr2 (geom 2 5))
(expect expr2 (* (* 1 5) 5))
(expect (eval expr2) 25)

;q4
;note:
;in "`(...)"
    ;-- ',' just deal with a agrument(num, symbol or list) in quasiquote
    ;-- after ',' deal with a agru, if it is a call exprssion, we will execute it
;'SchemeError' also is #t in builtin of 'or'
(define (make-or expr1 expr2)
    `(let ((v1 ,expr1))
        (if v1 v1 ,expr2))
)

;q5
;use "`" to make a quasiquotation of "(define (make-or expr1 expr2) `(let ((v1 ,expr1)) (if v1 v1 ,expr2)))"
(define (make-make-or)
  `(define (make-or expr1 expr2)
      `(let ((v1 ,expr1))
          (if v1 v1 ,expr2))
  )
)
