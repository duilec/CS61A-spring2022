(define (gcd a b)
    (if (= b 0)
        (abs a)
        (gcd b (modulo a b))
    )
)

(define (rational n d)
        ; find (+/-)gcd 
        (let ((g (if (> d 0)
                     (gcd n d)
                     (- (gcd n d))))
             )
          ; uses gcd to build a non-reduced fraction
          (list (/ n g) (/ d g))
        )
)

;solution
;rebuilt a new double tree, so, you should use 'tree'
;note: you don't need check that "it is a leaf?", because leaf also be rebuilded by 'map'
(define (double tr)
    ; Returns a tree identical to TR, but with all labels doubled.
    (tree 
        (* (label tr) 2)
        (map double (branches tr))
    )
)

(define tree1
        (tree 6
            (list (tree 3 (list (tree 1 nil)))
                    (tree 5 nil)
                    (tree 7 (list (tree 8 nil) (tree 9 nil))))
        )
)
                    
(expect tree1 (6 (3 (1)) (5) (7 (8) (9))))
(expect (double tree1) (12 (6 (2)) (10) (14 (16) (18))))