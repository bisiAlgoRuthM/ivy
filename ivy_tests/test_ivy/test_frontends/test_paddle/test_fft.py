# global
from hypothesis import given, strategies as st

# local
import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers import handle_frontend_test


# Custom Hypothesis strategy for generating sequences of 2 integers
def sequence_of_two_integers():
    return st.lists(st.integers(), min_size=2, max_size=2)


@handle_frontend_test(
    fn_tree="paddle.fft.fft",
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("valid"),
        min_value=-10,
        max_value=10,
        min_num_dims=1,
        min_dim_size=2,
        valid_axis=True,
        force_int_axis=True,
    ),
    n=st.one_of(
        st.integers(min_value=2, max_value=10),
        st.just(None),
    ),
    norm=st.sampled_from(["backward", "ortho", "forward"]),
)
def test_paddle_fft(
    dtype_x_axis,
    n,
    norm,
    frontend,
    backend_fw,
    test_flags,
    fn_tree,
):
    input_dtypes, x, axis = dtype_x_axis
    helpers.test_frontend_function(
        input_dtypes=input_dtypes,
        backend_to_test=backend_fw,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        x=x[0],
        n=n,
        axis=axis,
        norm=norm,
    )


@handle_frontend_test(
    fn_tree="paddle.fft.fftshift",
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("valid"),
        min_value=-10,
        max_value=10,
        min_num_dims=1,
        valid_axis=True,
        force_int_axis=True,
    ),
)
def test_paddle_fftshift(
    dtype_x_axis, frontend, test_flags, fn_tree, on_device, backend_fw
):
    input_dtype, x, axes = dtype_x_axis
    helpers.test_frontend_function(
        input_dtypes=input_dtype,
        backend_to_test=backend_fw,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        test_values=True,
        x=x[0],
        axes=axes,
    )


@handle_frontend_test(
    fn_tree="paddle.fft.hfft",
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("complex"),
        min_value=-10,
        max_value=10,
        min_num_dims=1,
        valid_axis=True,
        force_int_axis=True,
    ),
)
def test_paddle_hfft(
    dtype_x_axis,
    frontend,
    test_flags,
    fn_tree,
    on_device,
    backend_fw,
):
    input_dtype, x, axes = dtype_x_axis
    helpers.test_frontend_function(
        input_dtypes=input_dtype,
        backend_to_test=backend_fw,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        test_values=True,
        x=x[0],
        axes=axes,
    )


@given(
    s=st.one_of(
        st.none(), st.tuples(st.integers(min_value=1), st.integers(min_value=1))
    ),
    axis=st.one_of(st.none(), st.tuples(st.integers(min_value=-2, max_value=-1))),
    shape=st.lists(st.integers(min_value=1, max_value=10), min_size=2, max_size=2).map(
        tuple
    ),
)
@handle_frontend_test(
    fn_tree="paddle.fft.hfft2",
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("complex64"),
    ),
)
def test_paddle_hfft2(
    dtype_x_axis,
    s,
    axis,
    norm,
    frontend,
    backend_fw,
    test_flags,
    fn_tree,
    shape,
):
    input_dtypes, x, axis = dtype_x_axis
    x = x.reshape(shape)  # reshape x to the generated shape

    for norm in ["backward", "forward", "ortho"]:
        helpers.test_frontend_function(
            input_dtypes=input_dtypes,
            frontend=frontend,
            backend_to_test=backend_fw,
            test_flags=test_flags,
            fn_tree=fn_tree,
            x=x,
            s=s,
            axis=axis,
            norm=norm,
        )


@handle_frontend_test(
    fn_tree="paddle.fft.ifft",
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("valid"),
        min_value=-10,
        max_value=10,
        min_num_dims=1,
        min_dim_size=2,
        valid_axis=True,
        force_int_axis=True,
    ),
    n=st.one_of(
        st.integers(min_value=2, max_value=10),
        st.just(None),
    ),
    norm=st.sampled_from(["backward", "ortho", "forward"]),
)
def test_paddle_ifft(
    dtype_x_axis,
    n,
    norm,
    frontend,
    backend_fw,
    test_flags,
    fn_tree,
):
    input_dtypes, x, axis = dtype_x_axis
    helpers.test_frontend_function(
        input_dtypes=input_dtypes,
        frontend=frontend,
        backend_to_test=backend_fw,
        test_flags=test_flags,
        fn_tree=fn_tree,
        x=x[0],
        n=n,
        axis=axis,
        norm=norm,
    )


@handle_frontend_test(
    fn_tree="paddle.fft.ifftshift",
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("valid"),
        min_value=-10,
        max_value=10,
        min_num_dims=1,
        valid_axis=True,
        force_int_axis=True,
    ),
)
def test_paddle_ifftshift(
    dtype_x_axis,
    frontend,
    test_flags,
    fn_tree,
    on_device,
    backend_fw,
):
    input_dtype, x, axes = dtype_x_axis
    helpers.test_frontend_function(
        input_dtypes=input_dtype,
        backend_to_test=backend_fw,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        test_values=True,
        x=x[0],
        axes=axes,
    )


@handle_frontend_test(
    fn_tree="paddle.fft.irfft",
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("valid"),
        min_value=-10,
        max_value=10,
        min_num_dims=1,
        min_dim_size=2,
        valid_axis=True,
        force_int_axis=True,
    ),
    n=st.one_of(
        st.integers(min_value=2, max_value=10),
        st.just(None),
    ),
    norm=st.sampled_from(["backward", "ortho", "forward"]),
)
def test_paddle_irfft(
    dtype_x_axis,
    n,
    norm,
    frontend,
    test_flags,
    fn_tree,
    backend_fw,
):
    input_dtypes, x, axis = dtype_x_axis
    helpers.test_frontend_function(
        input_dtypes=input_dtypes,
        backend_to_test=backend_fw,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        x=x[0],
        n=n,
        axis=axis,
        norm=norm,
    )


@handle_frontend_test(
    fn_tree="paddle.fft.irfft2",
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("valid"),
        min_value=-10,
        max_value=10,
        min_num_dims=2,
        valid_axis=True,
        force_int_axis=True,
    ),
)
@given(st.data())
def test_paddle_irfft2(
    data,
    dtype_x_axis,
    frontend,
    test_flags,
    fn_tree,
    on_device,
    backend_fw,
):
    input_dtype, x, axes = dtype_x_axis
    for norm in ["backward", "forward", "ortho"]:
        s_values = data.draw(s_strategy)
        axes_values = data.draw(axes_strategy)

        # Ensure s and axes are sequences of 2 integers
        assert len(s_values) == 2
        assert len(axes_values) == 2

        # Convert s and axes to tuples as needed
        s = tuple(s_values)
        axes = tuple(axes_values)

        helpers.test_frontend_function(
            input_dtypes=input_dtype,
            frontend=frontend,
            backend_to_test=backend_fw,
            test_flags=test_flags,
            fn_tree=fn_tree,
            on_device=on_device,
            test_values=True,
            x=x[0],
            s=s,
            axes=axes,
            norm=norm,
        )


@handle_frontend_test(
    fn_tree="paddle.fft.irfftn",
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("complex"),
        min_value=-10,
        max_value=10,
        min_num_dims=1,
        max_num_dims=5,
        min_dim_size=2,
        max_dim_size=5,
        valid_axis=True,
        force_int_axis=True,
    ),
    norm=st.sampled_from(["backward", "ortho", "forward"]),
)
def test_paddle_irfftn(
    dtype_x_axis,
    norm,
    frontend,
    test_flags,
    fn_tree,
    backend_fw,
):
    input_dtypes, x, axis = dtype_x_axis
    helpers.test_frontend_function(
        input_dtypes=input_dtypes,
        backend_to_test=backend_fw,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        x=x[0],
        s=None,
        axes=None,
        norm=norm,
    )


@handle_frontend_test(
    fn_tree="paddle.fft.rfftfreq",
    n=st.integers(min_value=1, max_value=1000),
    sample_rate=st.integers(min_value=1, max_value=20),
)
def test_paddle_rfftfreq(
    n, sample_rate, backend_fw, frontend, test_flags, fn_tree, on_device
):
    d = 1 / sample_rate
    helpers.test_frontend_function(
        input_dtypes=[int],
        frontend=frontend,
        backend_to_test=backend_fw,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        test_values=True,
        n=n,
        d=d,
    )


# Use the custom strategy for s and axes
axes_strategy = sequence_of_two_integers()
s_strategy = sequence_of_two_integers()
