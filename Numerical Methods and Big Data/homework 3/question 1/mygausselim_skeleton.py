import numpy as np

## Code snippets you'll need in no particular order

#right-hand sides
#1) np.eye(n,n)
#2) A[i,k]/A[k,k]
#3) np.zeros(n)
#4) np.eye(n,n)
#5) A
#6) b[i]-L[i,k]*b[k]

#extended snippet
#1) d = np.empty_like(P[k,:])
#   d[:] = P[k,:]
#   P[k,:] = P[ind+k,:]
#   P[ind+k,:] = d

#indices
#1) k:n,k
#2) j
#3) 0:j,j

def mygausselim(A,b):
    ## Initialization
    n = A.shape[0]

    #Initialize L and P here: let L and P be an (nxn) identity matrix
    #-------- your code begins here--
    L = np.eye(n,n)
    P = np.eye(n,n)
    #-------- your code ends here ---

    #Initialize the solution vector x:
    #-------- your begins here-------
    x = np.zeros(n)
    #-------- your code ends here----

    ## LU factorization
    for k in range(n-1):
        ## Partial pivoting
        # Find the pivot line for column k
        # Search below kth entry in kth column
        # ----your code begins here: fill in the correct index slicing below -----
        ind = np.argmax(abs(A[k:n,k]))
        # ----your code ends here: fill in the correct index slicing below -----
    
        # Row swapping for A
        a_temp = np.empty_like(A[k,:])
        a_temp[:] = A[k,:]
        A[k,:] = A[ind+k,:]
        A[ind+k,:] = a_temp

        # Row swapping for L
        l_temp = np.empty_like(L[k,0:k])
        l_temp[:] = L[k,0:k]
        L[k,0:k] = L[ind+k,0:k]
        L[ind+k,0:k] = l_temp

        # Row swapping for b
        b_temp = b[k]
        b[k] = b[ind+k]
        b[ind+k] = b_temp
    
        # Row swapping for matrix P
        # --- your code begins here---
        d = np.empty_like(P[k,:])
        d[:] = P[k,:] 
        P[k,:] = P[ind+k,:]
        P[ind+k,:] = d
        # --- your code ends here -----
    
        #update the element of L
        for i in range(k+1,n):
            # ----- your code begins here: fill in the right hand side ---
            L[i,k] = A[i,k]/A[k,k]
            # ----- your code ends here: fill in the right hand side ---

        #update the elements of A and b
        for i in range(k+1,n):
            #update the lower-right submatrix of A
            A[i,k:n] = A[i,k:n]-L[i,k]*A[k,k:n]
        
            #update b
            # ----- your code begins here: fill in the right hand side ---
            b[i] = b[i]-L[i,k]*b[k]
            # ----- your code ends here: fill in the right hand side ---

    #Store the final result of U
    #-------- your begins here: fill the right hand side-------
    U = A
    #-------- your code ends here: fill the right hand side ----

    ## Back substitution
    for j in reversed(range(0,n)):
        x[j] = b[j]/A[j,j]
        # ----your code begins here: fill in the correct index slicing -----
        b[0:j] = b[0:j]-A[0:j,j]*x[j]
        # ----your code ends here: fill in the correct index slicing -----

    return [L, U, P, x]
