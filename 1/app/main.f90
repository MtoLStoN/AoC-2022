program main
  implicit none
  integer :: io_error,tmp,run,elv_no,line_inv
  integer :: inventory(10000)
  character,allocatable :: line(:)

  open(11,file="aoc_11.dat",iostat=io_error)

  tmp=0
  elv_no=1
  inventory(:)=0

  do while (io_error .eq. 0)
    read(11,'(I10)',iostat=io_error) line_inv
    write(*,*) line_inv
    if (line_inv .eq. 0) then
      inventory(elv_no)=tmp
      tmp=0
      elv_no=elv_no+1
      cycle
    end if
    !read(line,*) line_inv
    tmp=tmp+line_inv
  end do

  if (tmp .ne. 0) inventory(elv_no)=tmp
  
  tmp=MAXVAL(inventory)

  write(*,*) MAXLOC(inventory),MAXVAL(inventory)
  inventory(MAXLOC(inventory))=0 
  tmp=tmp+MAXVAL(inventory)
  write(*,*) MAXLOC(inventory),MAXVAL(inventory)
  inventory(MAXLOC(inventory))=0 
  tmp=tmp+MAXVAL(inventory)
  write(*,*) MAXLOC(inventory),MAXVAL(inventory)
  inventory(MAXLOC(inventory))=0 

  write(*,*) tmp

end program main
