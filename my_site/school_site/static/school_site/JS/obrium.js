$(document).ready(function() {
  $(".selA").change(function() {
  var selectedClass = $(this).children("option:selected").data("class");
  $(".selB option").each(function() {
  if ($(this).data("student") == selectedClass) {
  $(this).show();
  } else {
  $(this).hide();
  }
  });
  });
  });

 