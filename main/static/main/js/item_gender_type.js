(function($) {
    $(document).ready(function() {
        function updateTypeOptions(gender) {
            if (!gender) return;

            $.ajax({
                url: '/admin/main/item/get-types-by-gender/',
                data: { gender: gender },
                success: function(data) {
                    let options = '<option value="">---------</option>';
                    data.types.forEach(function(type) {
                        options += '<option value="' + type.id + '">' + type.name + '</option>';
                    });
                    $('#id_type').html(options);
                }
            });
        }

        const genderSelect = $('#id_gender');
        updateTypeOptions(genderSelect.val());

        genderSelect.on('change', function() {
            updateTypeOptions($(this).val());
        });
    });
})(django.jQuery);
