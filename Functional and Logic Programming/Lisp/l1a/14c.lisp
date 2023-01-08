;; c) sort a linear list with keeping the double values


; function to insert ith keeping doubles
; (defun my_insert (l e)
;     (cond
;         ((null l) (list e))
;         ((or (equal (car l) l) (< e (car l))) (cons e l))  ; the list has only one element OR e < head of l => (e l)
;         (T (cons (car l) (my_insert (cdr l) e)))
;     )
; )


; function to insert without keeping doubles
(defun my_insert (l e)
    (cond
        ((null l) (list e))				    ; if the list is empty, make a list out of the element to be inserted
        ((equal (car l) e) l)				; if the head of l is the element e, then the list is the result
        ((< e (car l)) (cons e l))			; if e is smaller than the head of l, make a cons with e and the list
        (T (cons (car l) (my_insert (cdr l) e)))	; recursive call
    )
)


(defun my_sort (l)					
    (cond		
        ((null l) nil)					; if the list is empty, there is nothing to sort
        (T (my_insert (my_sort (cdr l)) (car l)))	; sort the tail of l
							                        ; insert the new head of the sorted list into the result
    )
)

(defun test_my_sort ()
    (assert
	(and
	    (equal '(1 2 3 4 5 6 7 8 9) (my_sort '(9 9 8 8 7 7 6 6 5 5 4 4 3 3 2 2 1 1)))
	    (equal '(1 2 3 5 6 7 9) (my_sort '(1 3 2 5 6 7 7 3 9)))
	)
    )
)
