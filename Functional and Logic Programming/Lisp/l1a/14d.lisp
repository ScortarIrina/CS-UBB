;; d) Build a list which contains positions of a minimum numeric element from a given linear list.


(defun my_min (a b)
    (if (< a b) a b)
    (if (>= a b) b a)
)


(defun pos (l e i)
    (cond
        ((null l) nil)						;; l is empty
        ((equal (car l) e) (cons i (pos (cdr l) e (+ i 1))))	;; e = the head of l
								;; recursive call on the tail of l, with incremented position
        (T (pos (cdr l) e (+ i 1)))				;; recursive call
    )
)


(defun my_length (l)
    (cond
        ((atom l) 1)				;; the list is an atom => len(l)=1
        (T (apply '+ (mapcar 'my_length l)))	;; apply the funcion "mapcar" to the result retuned by "my_length"
    )
)



(defun min_list (l)
    (if (equal (my_length l) 1)			;; len(l)=1 
        (car l)					;; the min if the only element in l
    (my_min (car l) (min_list (cdr l)))		;; call my_min with the smallest elements
    )
)


(defun solve (l)
    (pos l (min_list l) 1)
)


(defun test_solve ()
    (assert
	    (and
	        (equal '(2 5 8) (solve '(3 2 5 6 2 7 7 2 3 9)))
	        (equal '(1 3 5) (solve '(1 33 1 23 1 2342342)))
	    )
    )
)
