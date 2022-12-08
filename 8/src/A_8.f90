module A_8
  implicit none
  private

  public :: is_visible, scenic_score
contains
  function is_visible(trees,x,y,direction)
    integer, allocatable, intent(in) :: trees(:,:)
    integer, intent(in) :: x,y
    character(len=*), intent(in) :: direction
    logical :: is_visible

    integer:: i

    is_visible=.true.
    select case(direction)
    case("N")
      do i=y+1,size(trees,2)
        if(trees(x,i) >= trees(x,y)) then
          is_visible=.false.
          exit
        end if
      end do
    case("O")
      do i=x+1,size(trees,1)
        if(trees(i,y) >= trees(x,y)) then
          is_visible=.false.
          exit
        end if
      end do
    case("S")
      do i=1,y-1
        if(trees(x,i) >= trees(x,y)) then
          is_visible=.false.
          exit
        end if
      end do
    case("W")
      do i=1,x-1
        if(trees(i,y) >= trees(x,y)) then
          is_visible=.false.
          exit
        end if
      end do
    end select
  end function is_visible

  function scenic_score(trees,x,y)
    integer, allocatable, intent(in) :: trees(:,:)
    integer, intent(in) :: x,y
    integer :: scenic_score

    integer:: i, N, O, S, W

    N=0
    O=0
    S=0
    W=0
    scenic_score=0

    !> N direction
    do i=y+1,size(trees,2)
      if(trees(x,i) < trees(x,y)) then
        N=N+1
      else
        N=N+1
        exit
      end if
    end do
    !> O direction
    do i=x+1,size(trees,1)
      if(trees(i,y) < trees(x,y)) then
        O=O+1
      else
        O=O+1
        exit
      end if
    end do
    !> S direction
    do i=1,y-1
      if(trees(x,(y-i)) < trees(x,y)) then
        S=S+1
      else
        S=S+1
        exit
      end if
    end do
    !> W direction
    do i=1,x-1
      if(trees((x-i),y) < trees(x,y)) then
        W=W+1
      else
        W=W+1
        exit
      end if
    end do

    scenic_score=N*O*S*W
  end function scenic_score
end module A_8
