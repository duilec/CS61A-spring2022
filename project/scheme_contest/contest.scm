;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: <Your title here>
;;;
;;; Description:
;;;   <It's your masterpiece.
;;;    Use these three lines to describe
;;;    its inner meaning.>

(define (draw)
  (ht)
  (speed 10)
  (define lx 30)
  (define rx 3)
  (define depth 21)
  (define step 10)
  (define pi 3.1415926535897932384626433832795028841971)
  (pu)
  (define (build d i x y theta)
    (goto x y)
    (seth (* -1 (- theta 90)))
    (if (< d depth)
      (if (odd? i)
        (begin
          (lt lx)
          (pd)
          (forward step)
          (pu)
          (build (+ d 1) (* i 2) 
            (+ x (* step (cos (/ (* pi (+ lx theta)) 180))))
            (+ y (* step (sin (/ (* pi (+ lx theta)) 180))))
            (+ lx theta)
          )
          (if (integer? (/ (- i 1) 3))
            (build (+ d 1) (/ (- i 1) 3) 
              (+ x (* step (cos (/ (* pi (+ lx theta)) 180))))
              (+ y (* step (sin (/ (* pi (+ lx theta)) 180))))
              (+ lx theta)
            )
          )
        )

        (begin
          (rt rx)
          (pd)
          (forward step)
          (pu)
          (build (+ d 1) (* i 2) 
            (+ x (* step (cos (/ (* pi (- theta rx)) 180))))
            (+ y (* step (sin (/ (* pi (- theta rx)) 180))))
            (- theta rx)
          )
          (if (integer? (/ (- i 1) 3))
            (build (+ d 1) (/ (- i 1) 3) 
              (+ x (* step (cos (/ (* pi (- theta rx)) 180))))
              (+ y (* step (sin (/ (* pi (- theta rx)) 180))))
              (- theta rx)
            )
          )
        )
      )
    )
  )

  (build 0 1 0 0 50)

  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)