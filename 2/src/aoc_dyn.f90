module aoc_dyn
    implicit none
    private

    public :: resize, shrink_array

    interface resize
        module procedure :: resize_int_array_1D
        module procedure :: resize_char_array_1D
    end interface resize

contains

!> Will resize an array to a certain size (n) or will it resize by about 1.5, can also initialize an array
subroutine resize_int_array_1D(arr,n)
    !> Array to resize
    integer, allocatable, intent(inout) :: arr(:)
    !> Number to resize to (optional)
    integer, optional, intent(in) :: n

    integer, allocatable :: tmp_arr(:)
    integer :: old_size, new_size
    integer :: i

    if (allocated(arr)) then
        old_size=size(arr)
        Call move_alloc(arr,tmp_arr)
    else
        old_size=20
    end if

    if (present(n)) then
        new_size=n
    else
        new_size=old_size + old_size/2 +1
    end if

    allocate(arr(new_size))

    if (allocated(tmp_arr)) then
        do i=1,min(size(tmp_arr),size(arr))
            arr(i)=tmp_arr(i)
        end do
    end if

end subroutine resize_int_array_1D

!> Will resize an array to a certain size (n) or will it resize by about 1.5, can also initialize an array
subroutine resize_char_array_1D(arr,n)
    !> Array to resize
    character(len=*), allocatable, intent(inout) :: arr(:)
    !> Number to resize to (optional)
    integer, optional, intent(in) :: n

    character(len=:), allocatable :: tmp_arr(:)
    integer :: old_size, new_size
    integer :: i

    if (allocated(arr)) then
        old_size=size(arr)
        Call move_alloc(arr,tmp_arr)
    else
        old_size=20
    end if

    if (present(n)) then
        new_size=n
    else
        new_size=old_size + old_size/2 +1
    end if

    allocate(arr(new_size))

    if (allocated(tmp_arr)) then
        do i=1,min(size(tmp_arr),size(arr))
            arr(i)=tmp_arr(i)
        end do
    end if

end subroutine resize_char_array_1D

subroutine shrink_array(arr,sort,position)
    !> Bit array to shrink
    integer, allocatable,intent(inout) :: arr(:,:)
    !> Number to look for
    integer, intent(in) :: sort
    !> Position of the sorting
    integer, intent(in) :: position
  
    integer, allocatable :: tmp_arr(:,:)
  
    integer :: i, count
  
    allocate(tmp_arr(size(arr,1),size(arr,2)))
  
    count=0
    do i=1,size(arr,1)
      if (arr (i,position) .eq. sort ) then
        count=count+1
        tmp_arr(count,:)=arr(i,:)
      end if
    end do
  
    !write(*,*) tmp_arr
    deallocate(arr)
    allocate(arr(count,size(tmp_arr,2)))
  
    do i=1,size(arr,1)
      arr(i,:)=tmp_arr(i,:)
    end do
  
  end subroutine shrink_array
  
end module aoc_dyn


