(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  ;(print (+ 1 2))
  (define (helper-enumerate s n)
    (cond
      ;you can't use '=', 'eq?' or 'equal?', you must use 'null?'
      ((null? s) nil) 
      ;you must use 'list' to build a pair of two-element 
      (else (cons (list n (car s)) (helper-enumerate (cdr s) (+ n 1)))) 
    )
  )
  (helper-enumerate s 0)
)
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to INORDER? and return
;; the merged lists.
(define (merge inorder? list1 list2)
  ; BEGIN PROBLEM 16
  (cond
    ((null? list1) list2)
    ((null? list2) list1)
    ((inorder? (car list1) (car list2)) (cons (car list1) (merge inorder? (cdr list1) list2)))
    (else (cons (car list2) (merge inorder? list1 (cdr list2))))
  )
)
  ; END PROBLEM 16


;; Optional Problem 1

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  ;expr maybe has sub_exprssion of 'let'
  ;we find it and handle it by using let-to-lambda recursivly
  (define (may_handle_let expr)
    (cond
      ((null? expr) nil)
      (else (cons (let-to-lambda (car expr)) (may_handle_let (cdr expr)) ))             
    )
  )
  ; atom and quote: directly return
  ; other: need rebuilting and checking
  (cond ((atom? expr)
         ; BEGIN PROBLEM 17
         expr
         ; END PROBLEM 17
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 17
         expr
         ; END PROBLEM 17
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
            (cons form (cons params (may_handle_let body)))
           ; END PROBLEM 17
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
           ; get names by list of two-elements(values)
          (define (names list)
            (cond
              ((null? list) nil)
              (else (cons (caar list) (names (cdr list))))
            )
          )
          ; get real_values by list of two-elements(values)
          (define (real_values list)
            (cond
              ((null? list) nil)
              (else (cons (car (cdar list)) (real_values (cdr list))))
            )
          )
          ;let-to-lambda
          (cons (cons 'lambda (cons (may_handle_let (names values)) 
                              (may_handle_let body))) 
                              (may_handle_let (real_values values)))
          ; END PROBLEM 17
           ))
        ; this is scheme list
        (else
         ; BEGIN PROBLEM 17
         (may_handle_let expr)
         ; END PROBLEM 17
         ))
)



;; Problem 21 (optional)
;; Draw the hax image using turtle graphics.
(define (hax d k)
  ; BEGIN Question 21
  'replace-this-line
  )
  ; END Question 21