program main
  use aoc_io, only: get_argument, read_input
  !use aoc_dyn, only: split
  implicit none

  character(len=:), allocatable :: input
  character(len=100), allocatable :: lines(:)
  character(len=1), allocatable :: doubles(:), badges(:)
  integer :: no_lines, half, full, tmp
  integer, allocatable :: quality(:)

  integer :: i,j,z,x

  Call get_argument(1,input)
  Call read_input(input,lines,no_lines)

  allocate(doubles(size(lines)))
  doubles(:)=""

  do i=1,size(lines)
    !Call split(trim(lines(i)),lhs,rhs)
    full=len(trim(lines(i)))
    half=full/2
    do j=1,half
      if (doubles(i) .ne. "") exit
      do z=half+1,full
        if (lines(i)(z:z) .eq. lines(i)(j:j)) then
          doubles(i) = lines(i)(z:z)
          exit
        end if
      end do
    end do
  end do

  allocate(badges(size(lines)/3))
  badges(:)=""

  do i=0,(size(lines)/3)-1
    do j=1,len(trim(lines(1+i*3)))
      do z=1,len(trim(lines(2+i*3)))
        do x=1,len(trim(lines(3+i*3)))
          if (lines(1+i*3)(j:j) .eq. lines(2+i*3)(z:z)) then
            if (lines(2+i*3)(z:z) .eq. lines(3+i*3)(x:x)) then
              badges(i+1)=lines(3+i*3)(x:x)
            end if
          end if
        end do
      end do
    end do
  end do
        

  allocate(quality(size(doubles)))

  do i=1,size(doubles)
    Call getquality(doubles(i),quality(i))
  end do

  write(*,*) sum(quality)
 deallocate(quality) 
  allocate(quality(size(badges)))
  do i=1,size(badges)
    Call getquality(badges(i),quality(i))
  end do

  write(*,*) sum(quality)

  
end program main

subroutine getquality(input,quality) 
  character(len=1), intent(in) :: input
  integer,intent(out) :: quality

  select case(input)
  case('a')
    quality=1
  case('b')
    quality=2
  case('c')
    quality=3
  case('d')
    quality=4
  case('e')
    quality=5
  case('f')
    quality=6
  case('g')
    quality=7
  case('h')
    quality=8
  case('i')
    quality=9
  case('j')
    quality=10
  case('k')
    quality=11
  case('l')
    quality=12
  case('m')
    quality=13
  case('n')
    quality=14
  case('o')
    quality=15
  case('p')
    quality=16
  case('q')
    quality=17
  case('r')
    quality=18
  case('s')
    quality=19
  case('t')
    quality=20
  case('u')
    quality=21
  case('v')
    quality=22
  case('w')
    quality=23
  case('x')
    quality=24
  case('y')
    quality=25
  case('z')
    quality=26
  case('A')
    quality=27
  case('B')
    quality=28
  case('C')
    quality=29
  case('D')
    quality=30
  case('E')
    quality=31
  case('F')
    quality=32
  case('G')
    quality=33
  case('H')
    quality=34
  case('I')
    quality=35
  case('J')
    quality=36
  case('K')
    quality=37
  case('L')
    quality=38
  case('M')
    quality=39
  case('N')
    quality=40
  case('O')
    quality=41
  case('P')
    quality=42
  case('Q')
    quality=43
  case('R')
    quality=44
  case('S')
    quality=45
  case('T')
    quality=46
  case('U')
    quality=47
  case('V')
    quality=48
  case('W')
    quality=49
  case('X')
    quality=50
  case('Y')
    quality=51
  case('Z')
    quality=52
  end select
end subroutine getquality