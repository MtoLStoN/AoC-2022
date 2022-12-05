module aoc_io
  use aoc_dyn, only: resize
  use iso_fortran_env, only: input_unit
  implicit none
  private

  public :: get_argument, read_input

contains
subroutine get_argument(iarg,arg)
  implicit none
  !> Number of argument to get
  integer, intent(in) :: iarg
  !> Argument to return
  character(len=:), allocatable, intent(out) :: arg

  !> Length of command argument
  integer :: arg_len

  Call get_command_argument(iarg,length=arg_len)
  allocate(character(len=arg_len) :: arg)
  Call get_command_argument(iarg,arg)
end subroutine get_argument

!> Read an input file into an array of lines
subroutine read_input(input,input_array,no_lines)
  !> Input File
  character(len=*), intent(in) :: input
  !> Array of lines of the input 
  character(len=*), allocatable, intent(out) :: input_array(:)
  !> Number of lines
  integer, intent(out), optional :: no_lines

  !> Error Handling
  integer :: io_error

  Call resize(input_array)

  open(input_unit,file=input,iostat=io_error)

  no_lines=0
  do while (io_error .eq. 0)
    no_lines=no_lines+1
    if (no_lines .gt. size(input_array)) Call resize(input_array)
    read(input_unit,'(a)',iostat=io_error) input_array(no_lines)
    if (io_error .ne. 0) no_lines=no_lines-1
  end do

  Call resize(input_array,no_lines)
end subroutine read_input

end module aoc_io
