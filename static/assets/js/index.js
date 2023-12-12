  const partitions = document.querySelectorAll('.partition');
  partitions.forEach(partition => {
    partition.addEventListener('mouseover', () => {
      partition.style.transform = 'scale(1.1)';
    });
    partition.addEventListener('mouseout', () => {
      partition.style.transform = 'scale(1)';
    });
  });