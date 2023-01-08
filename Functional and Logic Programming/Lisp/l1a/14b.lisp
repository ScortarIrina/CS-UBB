;; b) Write a function to return the product of all numerical atoms in a list,
;;    at any level.

(defun product_numerical_atoms (l)
    (cond 
        ((null l) 1)											;;   the list is empty, prod is 1
        ((listp (car l)) (* (product_numerical_atoms (car l)) (product_numerical_atoms (cdr l))))	;;   the head of the list is also a list
													                                                ;; compute the product of the innermost list,
													                                                ;; then the product of the whole list
        ((numberp (car l)) (* (car l) (product_numerical_atoms (cdr l))))	;;   the head of the list is a number, so we
													                        ;; compute the product of the head of l and 
													                        ;; go recursively into the tail of l
        (T (product_numerical_atoms (cdr l)))	                		    ;;  --- || --- || --- || --- || ---
    )
)


(defun test_product_numerical_atoms ()
     (assert
	    (and
		(equal 6 (product_numerical_atoms '(1 2 3)))
		(equal 90720 (product_numerical_atoms '(5 ( 1 2 3 (6 (8 9) 7)))))
	    )
    )
)
