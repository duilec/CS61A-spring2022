; City Abstraction
(define (make-city name lat lon)
  (cons name (cons lat (cons lon nil))))

(define (get-name city) (car city))

(define (get-lat city) (car (cdr city)))

(define (get-lon city) (car (cdr (cdr city))))

(define (distance city-a city-b) 
  'YOUR-CODE-HERE
  ; assigns value to x: (define x number)
  (define xa (get-lat city-a))
  (define ya (get-lon city-a))
  (define xb (get-lat city-b))
  (define yb (get-lon city-b))
  (sqrt (+ (expt (- xa xb) 2) (expt (- ya yb) 2)))
)

(define (closer-city lat lon city-a city-b)
  'YOUR-CODE-HERE
  (define city (make-city 'city lat lon))
  (define da (distance city city-a))
  (define db (distance city city-b))
  (if (< da db)
      (get-name city-a)
      (get-name city-b)
  )
)

; Teacher and Student Abstractions
(define (student-create name classes)
  (cons name classes))

(define (teacher-create name class students)
  (cons name (cons class students)))

(define (student-get-name student)
  'YOUR-CODE-HERE
  (car student)  
)

(define (student-get-classes student)
  'YOUR-CODE-HERE
  ; classes is a list!
  (cdr student)
)

(define (teacher-get-name teacher)
  'YOUR-CODE-HERE
  (car teacher)
)

(define (teacher-get-class teacher)
  'YOUR-CODE-HERE
  (car (cdr teacher))
)

(define (teacher-get-students teacher)
  'YOUR-CODE-HERE
  (cdr (cdr teacher))
)

(define (student-attend-class student class)
  'YOUR-CODE-HERE
  ; you should use 'cons' to cat a list
  ; you shouldn't use 'list' to separate lists
  (student-create (student-get-name student) (cons class (student-get-classes student) ))
)

(define (teacher-hold-class teacher)
;  'YOUR-CODE-HERE
  (define teacher-class (teacher-get-class teacher))
  (define teacher-students (teacher-get-students teacher))
  (define teacher-name (teacher-get-name teacher))
  ; form of map is (map f list), so map only with a agrument,
  ; so we bulid 'many-students-attend-class()' by 'student-attend-class()' to input a agrument
  (define (many-students-attend-class student)
    (student-attend-class student teacher-class)
  )
  (define new-students (map many-students-attend-class teacher-students))
  (define new-classes (map student-get-classes new-students))
  (teacher-create teacher-name new-classes new-students)
)

; Rational Abstraction
; Helpers
(define (cadr lst) (car (cdr lst)))

(define (gcd a b)
  (if (= b 0)
      (abs a)
      (gcd b (modulo a b))))

; Creates an object representing the rational number n/d
; Assume: n, d are integers and d != 0
; Note that this constructor simplifies the numerator and denominator
(define (rational n d)
  (let ((g (if (> d 0)
               (gcd n d)
               (- (gcd n d)))))
    (list (/ n g) (/ d g))))

; Gets the numerator of rational number r
(define (numer r) (car r))

; Gets the denominator of rational number r
(define (denom r) (cadr r))

; Adds two rational numbers x and y
(define (add-rational x y)
  (let ((new-num (+ (* (numer x) (denom y))
                    (* (numer y) (denom x))))
        (new-den (* (denom x) (denom y))))
    (rational new-num new-den)))

; Multiply two rational numbers x and y
(define (mul-rational x y)
  (let ((new-num (* (numer x) (numer y)))
        (new-den (* (denom x) (denom y))))
    (rational new-num new-den)))

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
