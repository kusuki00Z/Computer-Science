! Shengnan Zhou
! CSCI 305, Assignment 1 - Fortran Program
! Jan. 31, 2019



        PROGRAM firstFortran
        IMPLICIT NONE

        ! declare variables
        INTEGER :: MONEY=0, QUARTER=0, DIME=0, NICKEL=0, PENNY=0
        CHARACTER(LEN=30) :: QSTRING, DSTRING, NSTRING, PSTRING

        CHARACTER(LEN=8) :: DateINFO                   !ccyymmdd
        CHARACTER(LEN=4) :: Year, Month*2, Day*2
        CHARACTER(LEN=30) :: PrintTime
        CHARACTER(LEN=10) :: TimeINFO
        CHARACTER(LEN=2) :: Hour, Minute



        ! get date and time info
        CALL DATE_AND_TIME(DateINFO, TimeINFO)
        Year = DateINFO(1:4)
        Month = DateINFO(5:6)
        Day = DateINFO(7:8)

        Hour = TimeINFO(1:2)
        Minute = TimeINFO(3:4)

        ! print the date and time in the beginning
        WRITE(*,*)                              !print an empty line
        WRITE(*,*) 'Current date and time is: '
        PrintTime = Month//'-'//Day//'-'//Year//', '//Hour//':'//Minute
        WRITE(*,*) PrintTime
        WRITE(*,*)                              !print an empty line



        ! do-loop to get correcct input from user
        DO
                WRITE(*,*) "Enter the amount between 1-99: "
                READ(*,*) MONEY
                IF (0 <= MONEY .AND. MONEY <= 99) EXIT
                WRITE(*,*) "ERROR: Your input is out of range."
        END DO



        ! do-loop for converting input into coins
        DO 
                IF (MONEY == 0) EXIT            ! exit the loop

                IF (MONEY >= 25) THEN           ! convert to quarter
                        QUARTER = Conversion(MONEY, 25)
                        MONEY = MOD(MONEY, 25)
                ELSE IF (MONEY >= 10) THEN      ! convert to dime
                        DIME = Conversion(MONEY, 10)
                        MONEY = MOD(MONEY, 10)
                ELSE IF (MONEY >= 5) THEN       ! convert to nickel
                        NICKEL = Conversion(MONEY, 5)
                        MONEY = MOD(MONEY, 5)
                ELSE                            ! convert to penny
                        PENNY = Conversion(MONEY, 1)
                        MONEY = MOD(MONEY, 1)
                END IF
        END DO



        ! format results into strings
        IF (QUARTER > 0) THEN
                WRITE(QSTRING,"(I1, A)") QUARTER, ' quarter '
        ELSE
                QSTRING = ''
        END IF


        IF (DIME > 0) THEN
                WRITE(DSTRING, "(I1, A)") DIME, ' dime '
        ELSE
                DSTRING = ''
        END IF


        IF (NICKEL > 0) THEN
                WRITE(NSTRING, "(I1, A)") NICKEL, ' nickel '
        ELSE
                NSTRING = ''
        END IF


        IF (PENNY > 0) THEN
                WRITE(PSTRING, "(I1, A)") PENNY, ' penny '
        ELSE
                PSTRING = ''
        END IF


        ! print all the results
        WRITE(*,*)                      ! print an empty line
        WRITE(*,'(a)', ADVANCE='NO') trim(QSTRING) // " "
        WRITE(*,'(a)', ADVANCE='NO') trim(DSTRING) // " "
        WRITE(*,'(a)', ADVANCE='NO') trim(NSTRING) // " "
        WRITE(*,'(a)', ADVANCE='NO') trim(PSTRING) // " "
        WRITE(*,*)                      ! print an empty line



        CONTAINS
                INTEGER FUNCTION Conversion(m, a)
                        IMPLICIT NONE
                        INTEGER, INTENT(IN) :: m, a
                        Conversion = m / a
                END FUNCTION Conversion



        END PROGRAM firstFortran
