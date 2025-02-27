# SPDX-FileCopyrightText: Copyright (c) 2021-2022 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.


from imgui_bundle import imgui
import dnnlib
from gui_utils import imgui_utils


class LatentWidget:
    def __init__(self, viz):
        self.viz = viz
        self.latent = dnnlib.EasyDict(x=0, y=0)

    def drag(self, dx, dy):
        self.latent.x += dx / 1000
        self.latent.y += dy / 1000

    @imgui_utils.scoped_by_object_id
    def __call__(self, show=True):
        viz = self.viz
        if show:
            imgui.text("Latent")
            imgui.same_line()
            with imgui_utils.item_width(viz.font_size * 8):
                changed, (x_man, y_man) = imgui.input_float2("##xy", v=[self.latent.x, self.latent.y])
                if changed:
                    self.latent.x = x_man
                    self.latent.y = y_man

            imgui.same_line()
            _clicked, dragging, dx, dy = imgui_utils.drag_button("Drag", width=viz.button_w)
            if dragging:
                self.drag(dx, dy)

        viz.args.latent_x = self.latent.x
        viz.args.latent_y = self.latent.y
