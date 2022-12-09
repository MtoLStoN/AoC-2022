program main
  use A_9, only: bridge
  use aoc_io, only: read_input, get_argument
  implicit none
  character(len=:), allocatable :: input
  character(len=100), allocatable :: lines(:)
  integer :: no_lines, i, tmp1,tmp2, need(2)
  type(bridge) :: b
  character(len=1) :: direction
  integer :: steps

  Call get_argument(1, input)

  Call read_input(input, lines,no_lines)

  tmp1=0
  tmp2=0
  do i=1, no_lines
    read(lines(i),*) direction, steps
    select case(direction)
      case('R')
        tmp1 = tmp1+steps
        if (abs(tmp1) > need(1)) need(1) = abs(tmp1)
      case('L')
        tmp1 = tmp1-steps
        if (abs(tmp1) > need(1)) need(1) = abs(tmp1)
      case('U')
        tmp2 = tmp2+steps
        if (abs(tmp2) > need(2)) need(2) = abs(tmp2)
      case('D')
        tmp2 = tmp2-steps
        if (abs(tmp2) > need(2)) need(2) = abs(tmp2)
    end select
  end do
  need=need+1
  
  Call b%init(need(1)*2,need(2)*2,9)

  do i=1, no_lines
    read(lines(i),*) direction, steps
    Call b%move(direction, steps)
  end do

  write(*,*) count(b%visited(:,:,1))
  write(*,*) count(b%visited(:,:,9))

end program main

