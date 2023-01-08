;; a) union of 2 sets


(defun remove_first_appearance (l e)
    (cond 
        ((null l) nil)						    ;; the list is empty => false
        ((equal (car l) e) (cdr l))				    ;; the head of l is the element to be removed
        (T (cons (car l) (remove_first_appearance (cdr l) e)))	    ;; recursive call on the tail of the list l
    )
)


(defun union_sets (l1 l2)
    (cond
        ((and (null l1) (null l2)) nil)								;; both sets are empty => false
        ((null l1) l2)										;; l1 is empty => result is l2
        ((null l2) l1)  									;; l2 is empty => result is l1
        (T (cons (car l1) (union_sets (cdr l1) (remove_first_appearance l2 (car l1)))))		;; recursive call on the tail of l1
												;; remove the first appearance of the head of l1 in l2
    )
)



(defun test_union_sets ()
    (assert
	(and
	    (equal '(1 2 3) (union_sets '(1 2 3) '(1 2 3)))
	    (equal '(1 3 5 7 9 2 4 6 8 10) (union_sets '(1 3 5 7 9) '(2 4 6 8 10)))
	    (equal '(1 2 3 4 5 6 7 9) (union_sets '(1 2 3 4 5) '(1 5 6 7 9))) 
	)
    )
)
