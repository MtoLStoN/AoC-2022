program main
  use aoc_io, only: get_argument, read_input
  implicit none
  character(len=:), allocatable :: input
  character(len=100), allocatable :: lines(:)
  character(len=1), allocatable :: strategy(:,:)

  integer :: num_lines, i, points

  Call get_argument(1,input)
  Call read_input(input,lines,num_lines)

  allocate(strategy(num_lines,2))

  points=0

  do i=1,num_lines
    read(lines(i),*) strategy(i,1), strategy(i,2)
    select case(strategy(i,1))
    case ('A')
      select case(strategy(i,2))
      case ('X')
        points=points+3
      case('Y')
        points=points+4
      case('Z')
        points=points+8
      end select
    case ('B')
      select case(strategy(i,2))
      case ('X')
        points=points+1
      case('Y')
        points=points+5
      case('Z')
        points=points+9
      end select
    case ('C')
      select case(strategy(i,2))
      case ('X')
        points=points+2
      case('Y')
        points=points+6
      case('Z')
        points=points+7
      end select
    end select
  end do

  write(*,*) points

end program main
