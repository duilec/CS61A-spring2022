(define (cadr lst) (car (cdr lst)))

;I also define some helper function
(define (caar lst) (car (car lst)))
(define (cadar lst) (car (cdr (car lst))))

(define (make-kwlist1 keys values)
  ;'YOUR-CODE-HERE
  (list keys values)
)

(define (get-keys-kwlist1 kwlist) 
  ;'YOUR-CODE-HERE
  (car kwlist)
)

(define (get-values-kwlist1 kwlist)
  ;'YOUR-CODE-HERE
  (cadr kwlist)  
)

;note: about 'list'
;-- if it concat some elements, we will get a list
;-- if it concat some lists, we will get a nested list of lists
;note: about 'cons'
;-- if it concat some elements, we will get a list with '.'
;-- if it concat some lists, we will get a list of lists
;-- 'cons' end of 'nil', we must assign it
;to make kwlist2 we mixed 'list' and 'cons'
(define (make-kwlist2 keys values)
  ;'YOUR-CODE-HERE
  (define (built-pair key value)
    (list key value)
  )
  (if (null? keys)
    nil
    (cons (built-pair (car keys) (car values)) (make-kwlist2 (cdr keys) (cdr values)))
  )
)

(define (get-keys-kwlist2 kwlist) 
  ;'YOUR-CODE-HERE
  (if (null? kwlist)
    nil
    (cons (caar kwlist) (get-keys-kwlist2 (cdr kwlist)))
  )
)

(define (get-values-kwlist2 kwlist)
  'YOUR-CODE-HERE
  (if (null? kwlist)
    nil
    (cons (cadar kwlist) (get-values-kwlist2 (cdr kwlist)))
  )
)
;my solution: remeber "abstraction barrier" in mind, it is elegant
;we get the "second" that the second element of the first list
;-- if "second" is number, it is type of kwlist2
;-- if "second" is not number, it is type of kwlist1
(define (add-to-kwlist kwlist key value)
  'YOUR-CODE-HERE
  (define second (cadar kwlist))
  (if (number? second)
    (make-kwlist2 (append (get-keys-kwlist2 kwlist)  (cons key nil)) 
                  (append (get-values-kwlist2 kwlist) (cons value nil)))
    (make-kwlist1 (append (get-keys-kwlist1 kwlist)  (cons key nil)) 
                  (append (get-values-kwlist1 kwlist) (cons value nil)))
  )
)

;my solution: not remeber "abstraction barrier" in mind, it is not elegant
;I do some useless works in different abstraction(type-list1 or type-list2)
;but it is clear when checking
;(define (add-to-kwlist kwlist key value)
;  'YOUR-CODE-HERE
;  (define second (cadar kwlist))
;  (define lst1-keys (append (get-keys-kwlist1 kwlist)  (cons key nil)))
;  (define lst1-values (append (get-values-kwlist1 kwlist) (cons value nil)))
;  (define new-lst2 (append kwlist (cons (list key value) nil)))
;  (if (number? second)
;    new-lst2
;    (make-kwlist1 lst1-keys lst1-values)
;  )
;)
 
(define (get-first-from-kwlist kwlist key)
  'YOUR-CODE-HERE
  (define second (cadar kwlist))
  (define (get-first key keys values)
    (cond
      ((null? keys) nil)
      ((eq? key (car keys)) (car values))
      (else (get-first key (cdr keys) (cdr values)))
    )
  )
  (if (number? second)
    (get-first key (get-keys-kwlist2 kwlist) (get-values-kwlist2 kwlist))
    (get-first key (get-keys-kwlist1 kwlist) (get-values-kwlist1 kwlist))
  )
)

;my solution
;even: 0 ==> be pruned
;odd: 1 ==> be left
(define (prune-expr expr)
  (define (prune-helper lst is-odd) 
  'YOUR-CODE-HERE
  (cond
    ((null? lst) nil)
    ((= is-odd 1) (cons (car lst) (prune-helper (cdr lst) (- is-odd 1))))
    (else (prune-helper (cdr lst) (+ is-odd 1)))
  )
)
  'YOUR-CODE-HERE
  (cons (car expr) (prune-helper (cdr expr) 1))
)
;reference solution
;use "(cdr (cdr lst)" to get element of odd
;(define (prune-expr expr)
;  (define (prune-helper lst)
;    (if (or (null? lst) (null? (cdr lst)))
;        lst
;        (cons (car lst) (prune-helper (cdr (cdr lst))))))
;  (cons (car expr) (prune-helper (cdr expr))))

;note: about 'list'
;-- if it concat some elements, we will get a list
;-- if it concat some lists, we will get a nested list of lists
(define (curry-cook formals body) 
  'YOUR-CODE-HERE
  (if (null? (cdr formals)) 
    (list 'lambda (list (car formals)) body)
    (list 'lambda (list (car formals)) (curry-cook (cdr formals) body))
  )
)

;consume all args, passes one element each time
(define (curry-consume curries args)
  'YOUR-CODE-HERE
  (if (null? args)
    curries
    (curry-consume (curries (car args)) (cdr args))
  )
)
