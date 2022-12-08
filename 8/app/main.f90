program main
  use aoc_io, only: get_argument, read_input 
  use A_8, only: is_visible, scenic_score
  implicit none
  character(len=:), allocatable :: input
  character(len=100), allocatable :: lines(:)
  integer :: no_lines

  integer, allocatable :: trees(:,:), scores(:,:)

  integer :: i, j, visibles

  Call get_argument(1,input)
  Call read_input(input,lines,no_lines)
  allocate(trees(len(trim(lines(1))),no_lines))
  allocate(scores(len(trim(lines(1))),no_lines))

  do i=1,no_lines
    do j=1,len(trim(lines(i)))
      read(lines(i)(j:j),*) trees(j,(no_lines-i)+1)
    end do
  end do

  visibles=0
  do i=1,no_lines
    do j=1,len(trim(lines(i)))
      if (is_visible(trees,j,i,"N")) then
        visibles=visibles+1
      else if (is_visible(trees,j,i,"O")) then
        visibles=visibles+1
      else if (is_visible(trees,j,i,"S")) then
        visibles=visibles+1
      else if (is_visible(trees,j,i,"W")) then
        visibles=visibles+1
      end if
      scores(j,i)=scenic_score(trees,j,i)
    end do
  end do

  
  write(*,*) visibles
  write(*,*) maxval(scores)

end program main
