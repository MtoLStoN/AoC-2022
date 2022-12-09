module A_9
  implicit none
  private

  public :: bridge


  type bridge
    !> Has the tail visited this field?
    logical, allocatable :: visited(:,:,:)
    !> Is the tail X on this field?
    logical,allocatable :: tail(:,:,:)
    !> Is the head on this field?
    logical, allocatable :: head(:,:)
    contains
      procedure :: update_tail
      procedure :: move
      procedure :: init
  end type bridge

contains

  !> Initialize the bridge
  subroutine init(self,x,y,knots)
    class(bridge), intent(inout) :: self
    integer, intent(in) :: x, y
    integer, intent(in) :: knots


    allocate(self%tail(x,y,knots))
    allocate(self%head(x,y))
    allocate(self%visited(x,y,knots))

    self%visited(:,:,:) = .false.
    self%tail(:,:,:) = .false.
    self%head(:,:) = .false.

    self%tail(x/2,y/2,:) = .true.
    self%head(x/2,y/2) = .true.
    self%visited(x/2,y/2,:) = .true.

  end subroutine init

  !> Move the head in a given direction
  subroutine move(self,direction,steps)
    class(bridge), intent(inout) :: self
    character(len=1), intent(in) :: direction
    integer, intent(in) :: steps

    integer :: act_step
    integer :: headx, heady, head(2), j


    do act_step=1,steps
      head=findloc(self%head,.true.)
      headx=head(1)
      heady=head(2)
      select case(direction)
        case('U')
          self%head(headx,heady) = .false.
          self%head(headx,heady+1) = .true.
        case('D')
          self%head(headx,heady) = .false.
          self%head(headx,heady-1) = .true.
        case('R')
          self%head(headx,heady) = .false.
          self%head(headx+1,heady) = .true.
        case('L')
          self%head(headx,heady) = .false.
          self%head(headx-1,heady) = .true.
      end select
      do j= 1,size(self%tail,dim=3)
        Call self%update_tail(j)
      end do
    end do

  end subroutine move

  !> Update the tail
  subroutine update_tail(self,knot)
    class(bridge), intent(inout) :: self
    integer, intent(in) :: knot

    !> Coordinates of the tail
    integer :: tailx, taily, tail(2)
    !> Coordinates of the head
    integer :: headx, heady, head(2)
    !> Difference between head and tail
    integer :: diffx, diffy

    !> Where is the tail?
    tail=findloc(self%tail(:,:,knot),.true.)
    tailx=tail(1)
    taily=tail(2)

    !> Where is the head?
    if (knot == 1) then
      head=findloc(self%head,.true.)
    else
      head=findloc(self%tail(:,:,knot-1),.true.)
    end if
    headx=head(1)
    heady=head(2)

    !> If the tail is not right next to the head, move it
    diffx=headx-tailx
    diffy=heady-taily

  
    !> I know these moves are terribly coded, but that diagonal ones really got to me ;)
    if (diffx > 1 .and. diffy > 1) then
      !> Completely diagonal move
      self%tail(tailx,taily,knot) = .false.
      self%tail(tailx+(diffx-1),taily+(diffy-1),knot) = .true.
      self%visited(tailx+(diffx-1),taily+(diffy-1),knot) = .true.
      return
    end if  
    if (diffx > 1 .and. diffy < -1) then
      !> Completely diagonal move
      self%tail(tailx,taily,knot) = .false.
      self%tail(tailx+(diffx-1),taily+(diffy+1),knot) = .true.
      self%visited(tailx+(diffx-1),taily+(diffy+1),knot) = .true.
      return
    end if  
    if (diffx < -1 .and. diffy < -1) then
      !> Completely diagonal move
      self%tail(tailx,taily,knot) = .false.
      self%tail(tailx+(diffx+1),taily+(diffy+1),knot) = .true.
      self%visited(tailx+(diffx+1),taily+(diffy+1),knot) = .true.
      return
    end if 
    if (diffx < -1 .and. diffy > 1) then
      !> Completely diagonal move
      self%tail(tailx,taily,knot) = .false.
      self%tail(tailx+(diffx+1),taily+(diffy-1),knot) = .true.
      self%visited(tailx+(diffx+1),taily+(diffy-1),knot) = .true.
      return
    end if  
    if (diffx > 1) then
      !> Move the tail in x direction
      self%tail(tailx,taily,knot) = .false.
      self%tail(tailx+(diffx-1),taily+diffy,knot) = .true.
      self%visited(tailx+(diffx-1),taily+diffy,knot) = .true.
      return
    end if
    if (diffx < -1) then
      !> Move the tail in -x direction
      self%tail(tailx,taily,knot) = .false.
      self%tail(tailx+(diffx+1),taily+diffy,knot) = .true.
      self%visited(tailx+(diffx+1),taily+diffy,knot) = .true.
      return
    end if
    if (diffy > 1) then
      !> Move the tail in y direction
      self%tail(tailx,taily,knot) = .false.
      self%tail(tailx+diffx,taily+(diffy-1),knot) = .true.
      self%visited(tailx+diffx,taily+(diffy-1),knot) = .true.
      return
    end if
    if (diffy < -1) then
      !> Move the tail in -y direction
      self%tail(tailx,taily,knot) = .false.
      self%tail(tailx+diffx,taily+(diffy+1),knot) = .true.
      self%visited(tailx+diffx,taily+(diffy+1),knot) = .true.
      return
    end if

  end subroutine update_tail

end module A_9