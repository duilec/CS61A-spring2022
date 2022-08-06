(define (split-at lst n) 
  'YOUR-CODE-HERE
  (define (car-part lst n)
    (cond
      ((null? lst) nil)
      ((> n 0) (cons (car lst) (car-part (cdr lst) (- n 1))))
      (else (car-part (cdr lst) (- n 1)))
    )
  )
  (define (cdr-part lst n len)
    (cond
      ((null? lst) nil)
      ((= n len) (cons (car lst) (cdr-part (cdr lst) (+ n 1) (+ len 1))))
      (else (cdr-part (cdr lst) n (+ len 1)))
    )
  )
  (cons (car-part lst n) (cdr-part lst n 0))
)

; reference
; using "(cdr lst)" recursivly get to the part of bigger than n
(define (split-at lst n)
  (cond 
    ((= n 0)
     (cons nil lst))
    ((null? lst)
     (cons lst nil))
    (else
     (let ((rec (split-at (cdr lst) (- n 1))))
       (cons (cons (car lst) (car rec)) (cdr rec))))))

; Tree Abstraction
; Constructs tree given label and list of branches
(define (tree label branches)
  (cons label branches))

; Returns the label of the tree
(define (label t) (car t))

; Returns the list of branches of the given tree
(define (branches t) (cdr t))

; Returns #t if t is a leaf, #f otherwise
(define (is-leaf t) (null? (branches t)))

; note: just replace!
(define (filter-odd t) 
  'YOUR-CODE-HERE
  ; we have function of "odd?" and "even?"
  (cond
    ((null? t) nil)
    ((odd? (label t)) (tree (label t) (map filter-odd (branches t))))
    (else (tree nil (map filter-odd (branches t))))
  )
)

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (swap expr) 
  'YOUR-CODE-HERE
  (define operator (car expr))
  (define expr1 (cadr expr))
  (define expr2 (caddr expr))
  (define rest (cdr(cddr expr)))
  
  ; note: atom(boolean, number, symbol, string, or nil) also can be evaluate then return itself
  ; compare then maybe bulid a new list
  (if (> (eval expr2) (eval expr1))
    (cons operator (cons expr2 (cons expr1 rest)))
    expr
  )
)

; reference
; using "let"
;(define (swap expr)
;  (let ((op (car expr))
;        (first (car (cdr expr)))
;        (second (caddr expr))
;        (rest (cdr (cddr expr))))
;    (if (> (eval second) (eval first))
;        (cons op (cons second (cons first rest)))
;        expr)))
