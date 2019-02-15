; Shengnan Zhou
; CSCI 305, Assignment 2 - Lisp Program
; Feb. 13, 2019
; --------------------------------------
; sumList: this function will get the 
; summation of the input list. This 
; function can deal with nested list.
; --------------------------------------
; consecSum: this function will get the
; summation of three consecutive elements
; from the input list. This function 
; cannot deal with nested list.
; --------------------------------------
; Please manually enter the list below.



; recursive function to sum the list
(defun sumList (lst)
  (cond ((null lst) 0)				; return 0 if list is empty
	((atom lst) lst)			; return the only atom
	((list lst) (+ (sumList (car lst)) 	; allow to read nested list
			    (sumList (cdr lst))))
   )
 )



; recursive function to find the highest sum of three consecutive numbers
; setup variables
(setq temp 0)
(setq result 0)

(defun consecSum(lst)
  (cond ((null lst) 0)
	((atom lst) lst)
	((= (list-length lst) 2) (return-from consecSum result))
	((> (list-length lst) 2) (setq temp (+ (nth 0 lst) 
					       (nth 1 lst) 
					       (nth 2 lst)))
				 (if (<= result temp)
				   (setq result temp)
				  )
				 (consecSum (cdr lst))
	 )
   )
 )



; write out results
(write-line "The sum of the list is: ")
;please enter the list here
(write(sumList '(-2 4 -3 5 -3 1 -2 3)))		
(terpri)
(write-line "")
(write-line "The highest sum of three consecutive numbers in the list is: ")
;please enter the list here
(write(consecSum '(-2 4 -3 5 -3 1 -2 3)))
(terpri)





